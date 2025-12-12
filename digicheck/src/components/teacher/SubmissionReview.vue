<template>
  <div class="submission-review">
    <!-- Header -->
    <div class="review-header">
      <div class="student-info">
        <h4>{{ submission.student_name }}</h4>
        <p>{{ submission.quiz_title }} - {{ submission.quiz_code }}</p>
        <div class="meta-info">
          <span>Submitted: {{ formatDateTime(submission.submitted_at) }}</span>
          <span>Time Taken: {{ submission.time_taken_minutes }} minutes</span>
        </div>
      </div>
      <div class="score-info">
        <div class="score-display">
          <div class="score" :class="getScoreClass(submission.percentage)">
            {{ submission.percentage }}%
          </div>
          <div class="fraction">{{ submission.total_score }}/{{ submission.max_score }} pts</div>
        </div>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="loading-container">
      <div class="spinner"></div>
      <p>Loading submission details...</p>
    </div>

    <!-- Questions and Answers -->
    <div v-else class="questions-section">
      <div v-for="(answer, index) in studentAnswers" :key="answer.id" class="question-block">
        <div class="question-header">
          <span class="question-number">Question {{ index + 1 }}</span>
          <span class="question-type">{{ formatQuestionType(answer.question_type) }}</span>
          <div class="points-info">
            <span class="points-earned" :class="{ correct: answer.is_correct }">
              {{ answer.points_earned }}/{{ answer.points_possible }} pts
            </span>
          </div>
        </div>

        <div class="question-content">
          <div class="question-text">{{ answer.question_text }}</div>

          <!-- Multiple Choice -->
          <div v-if="answer.question_type === 'multiple_choice'" class="answer-section">
            <div class="options-list">
              <div 
                v-for="option in answer.options" 
                :key="option.id"
                class="option-item"
                :class="{
                  'selected': option.id === answer.selected_option_id,
                  'correct': option.is_correct,
                  'incorrect': option.id === answer.selected_option_id && !option.is_correct
                }"
              >
                <span class="option-letter">{{ String.fromCharCode(65 + option.option_number - 1) }}</span>
                <span class="option-text">{{ option.option_text }}</span>
                <div class="option-indicators">
                  <i v-if="option.is_correct" class="fas fa-check correct-indicator"></i>
                  <i v-if="option.id === answer.selected_option_id" class="fas fa-user-check selected-indicator"></i>
                </div>
              </div>
            </div>
          </div>

          <!-- True/False or Fill in Blank -->
          <div v-else class="answer-section">
            <div class="answer-comparison">
              <div class="student-answer">
                <label>Student Answer:</label>
                <div class="answer-value" :class="{ correct: answer.is_correct, incorrect: !answer.is_correct }">
                  {{ answer.answer_text || 'No answer provided' }}
                </div>
              </div>
              <div class="correct-answer">
                <label>Correct Answer:</label>
                <div class="answer-value correct">{{ answer.correct_answer }}</div>
              </div>
            </div>
          </div>

          <!-- Manual Review Section -->
          <div v-if="answer.requires_manual_review || answer.question_type === 'fill_blank'" class="manual-review">
            <div class="review-controls">
              <label>Manual Review:</label>
              <div class="grade-controls">
                <button 
                  @click="markCorrect(answer)" 
                  class="btn-grade"
                  :class="{ active: answer.is_correct }"
                >
                  <i class="fas fa-check"></i> Correct
                </button>
                <button 
                  @click="markIncorrect(answer)" 
                  class="btn-grade"
                  :class="{ active: !answer.is_correct }"
                >
                  <i class="fas fa-times"></i> Incorrect
                </button>
              </div>
            </div>
            <div class="comment-section">
              <label>Teacher Comment (Optional):</label>
              <textarea 
                v-model="answer.teacher_comment"
                @blur="updateComment(answer)"
                placeholder="Add a comment for this answer..."
                rows="2"
              ></textarea>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Overall Feedback -->
    <div class="feedback-section">
      <label>Overall Feedback:</label>
      <textarea 
        v-model="overallFeedback"
        @blur="updateOverallFeedback"
        placeholder="Provide overall feedback for this submission..."
        rows="4"
      ></textarea>
    </div>

    <!-- Actions -->
    <div class="review-actions">
      <button @click="saveReview" class="btn-save" :disabled="saving">
        <i class="fas fa-save"></i>
        {{ saving ? 'Saving...' : 'Save Review' }}
      </button>
      <button @click="finalizeGrade" class="btn-finalize" :disabled="saving">
        <i class="fas fa-check-circle"></i>
        Finalize Grade
      </button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue'
import { supabase } from '../../supabase.js'

export default {
  name: 'SubmissionReview',
  props: {
    submission: {
      type: Object,
      required: true
    }
  },
  emits: ['submission-updated', 'close'],
  setup(props, { emit }) {
    const loading = ref(true)
    const saving = ref(false)
    const studentAnswers = ref([])
    const overallFeedback = ref('')

    const fetchSubmissionDetails = async () => {
      try {
        loading.value = true

        // Fetch student answers with question details
        const { data: answers, error: answersError } = await supabase
          .from('student_answers')
          .select(`
            id,
            selected_option_id,
            answer_text,
            is_correct,
            points_earned,
            points_possible,
            teacher_comment,
            requires_manual_review,
            quiz_questions!inner (
              id,
              question_text,
              question_type,
              points
            )
          `)
          .eq('attempt_id', props.submission.id)
          .order('quiz_questions.question_number')

        if (answersError) throw answersError

        // For each answer, fetch additional details based on question type
        const detailedAnswers = await Promise.all(
          answers.map(async (answer) => {
            const questionDetails = {
              id: answer.id,
              question_id: answer.quiz_questions.id,
              question_text: answer.quiz_questions.question_text,
              question_type: answer.quiz_questions.question_type,
              points_possible: answer.points_possible,
              points_earned: answer.points_earned,
              is_correct: answer.is_correct,
              selected_option_id: answer.selected_option_id,
              answer_text: answer.answer_text,
              teacher_comment: answer.teacher_comment || '',
              requires_manual_review: answer.requires_manual_review
            }

            if (answer.quiz_questions.question_type === 'multiple_choice') {
              // Fetch options for multiple choice
              const { data: options, error: optionsError } = await supabase
                .from('question_options')
                .select('*')
                .eq('question_id', answer.quiz_questions.id)
                .order('option_number')

              if (optionsError) throw optionsError
              questionDetails.options = options
            } else {
              // Fetch correct answer for other types
              const { data: correctAnswer, error: correctAnswerError } = await supabase
                .from('question_answers')
                .select('correct_answer')
                .eq('question_id', answer.quiz_questions.id)
                .single()

              if (correctAnswerError) throw correctAnswerError
              questionDetails.correct_answer = correctAnswer.correct_answer
            }

            return questionDetails
          })
        )

        studentAnswers.value = detailedAnswers
        overallFeedback.value = props.submission.teacher_feedback || ''

      } catch (error) {
        console.error('Error fetching submission details:', error)
      } finally {
        loading.value = false
      }
    }

    const markCorrect = async (answer) => {
      answer.is_correct = true
      answer.points_earned = answer.points_possible
      await updateAnswer(answer)
    }

    const markIncorrect = async (answer) => {
      answer.is_correct = false
      answer.points_earned = 0
      await updateAnswer(answer)
    }

    const updateAnswer = async (answer) => {
      try {
        const { error } = await supabase
          .from('student_answers')
          .update({
            is_correct: answer.is_correct,
            points_earned: answer.points_earned,
            teacher_comment: answer.teacher_comment
          })
          .eq('id', answer.id)

        if (error) throw error

        // Recalculate total score
        await recalculateScore()
      } catch (error) {
        console.error('Error updating answer:', error)
      }
    }

    const updateComment = async (answer) => {
      try {
        const { error } = await supabase
          .from('student_answers')
          .update({
            teacher_comment: answer.teacher_comment
          })
          .eq('id', answer.id)

        if (error) throw error
      } catch (error) {
        console.error('Error updating comment:', error)
      }
    }

    const updateOverallFeedback = async () => {
      try {
        const { error } = await supabase
          .from('quiz_attempts')
          .update({
            teacher_feedback: overallFeedback.value
          })
          .eq('id', props.submission.id)

        if (error) throw error
      } catch (error) {
        console.error('Error updating feedback:', error)
      }
    }

    const recalculateScore = async () => {
      const totalEarned = studentAnswers.value.reduce((sum, answer) => sum + answer.points_earned, 0)
      const totalPossible = studentAnswers.value.reduce((sum, answer) => sum + answer.points_possible, 0)
      const percentage = totalPossible > 0 ? Math.round((totalEarned / totalPossible) * 100) : 0

      try {
        const { error } = await supabase
          .from('quiz_attempts')
          .update({
            total_score: totalEarned,
            percentage: percentage,
            status: 'reviewed',
            manually_reviewed: true
          })
          .eq('id', props.submission.id)

        if (error) throw error

        // Update local submission data
        emit('submission-updated', {
          id: props.submission.id,
          total_score: totalEarned,
          percentage: percentage,
          status: 'reviewed',
          teacher_feedback: overallFeedback.value
        })
      } catch (error) {
        console.error('Error recalculating score:', error)
      }
    }

    const saveReview = async () => {
      try {
        saving.value = true
        await recalculateScore()
        await updateOverallFeedback()
        alert('Review saved successfully!')
      } catch (error) {
        console.error('Error saving review:', error)
        alert('Error saving review. Please try again.')
      } finally {
        saving.value = false
      }
    }

    const finalizeGrade = async () => {
      if (!confirm('Finalize this grade? This will make it visible to the student.')) {
        return
      }

      try {
        saving.value = true
        await saveReview()
        
        // Finalize the grade
        const { error } = await supabase.rpc('finalize_quiz_results', {
          p_quiz_id: props.submission.quiz_id
        })

        if (error) throw error

        alert('Grade finalized successfully!')
        emit('close')
      } catch (error) {
        console.error('Error finalizing grade:', error)
        alert('Error finalizing grade. Please try again.')
      } finally {
        saving.value = false
      }
    }

    // Utility functions
    const formatDateTime = (dateString) => {
      return new Date(dateString).toLocaleString()
    }

    const formatQuestionType = (type) => {
      const typeMap = {
        multiple_choice: 'Multiple Choice',
        true_false: 'True/False',
        fill_blank: 'Fill in the Blank'
      }
      return typeMap[type] || type
    }

    const getScoreClass = (percentage) => {
      if (percentage >= 90) return 'excellent'
      if (percentage >= 80) return 'good'
      if (percentage >= 70) return 'average'
      return 'needs-improvement'
    }

    onMounted(() => {
      fetchSubmissionDetails()
    })

    return {
      loading,
      saving,
      studentAnswers,
      overallFeedback,
      markCorrect,
      markIncorrect,
      updateComment,
      updateOverallFeedback,
      saveReview,
      finalizeGrade,
      formatDateTime,
      formatQuestionType,
      getScoreClass
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.submission-review {
  padding: 1.5rem;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e2e8f0;
}

.student-info h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  color: #1a202c;
}

.student-info p {
  margin: 0 0 0.5rem 0;
  color: #64748b;
  font-weight: 500;
}

.meta-info {
  display: flex;
  gap: 1rem;
  font-size: 0.875rem;
  color: #64748b;
}

.score-info .score-display {
  text-align: right;
}

.score {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.score.excellent { color: #059669; }
.score.good { color: #0369a1; }
.score.average { color: #d97706; }
.score.needs-improvement { color: #dc2626; }

.fraction {
  font-size: 0.875rem;
  color: #64748b;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #64748b;
}

.spinner {
  width: 30px;
  height: 30px;
  border: 3px solid #e2e8f0;
  border-top: 3px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.question-block {
  background: #f8fafc;
  border-radius: 0.5rem;
  margin-bottom: 1.5rem;
  overflow: hidden;
}

.question-header {
  background: white;
  padding: 1rem;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.question-number {
  font-weight: 600;
  color: #1a202c;
}

.question-type {
  background: #e0f2fe;
  color: #0369a1;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 500;
}

.points-earned {
  font-weight: 600;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
}

.points-earned.correct {
  background: #dcfce7;
  color: #16a34a;
}

.question-content {
  padding: 1rem;
}

.question-text {
  font-size: 1rem;
  color: #1a202c;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border-radius: 0.5rem;
  border: 2px solid transparent;
  background: white;
}

.option-item.selected {
  border-color: #3b82f6;
  background: #eff6ff;
}

.option-item.correct {
  background: #dcfce7;
  border-color: #16a34a;
}

.option-item.incorrect {
  background: #fef2f2;
  border-color: #dc2626;
}

.option-letter {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
}

.option-text {
  flex: 1;
}

.option-indicators {
  display: flex;
  gap: 0.5rem;
}

.correct-indicator {
  color: #16a34a;
}

.selected-indicator {
  color: #3b82f6;
}

.answer-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.student-answer label,
.correct-answer label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #374151;
}

.answer-value {
  padding: 0.75rem;
  border-radius: 0.5rem;
  font-weight: 500;
}

.answer-value.correct {
  background: #dcfce7;
  color: #16a34a;
  border: 1px solid #bbf7d0;
}

.answer-value.incorrect {
  background: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}

.manual-review {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}

.review-controls {
  margin-bottom: 1rem;
}

.review-controls label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #374151;
}

.grade-controls {
  display: flex;
  gap: 0.5rem;
}

.btn-grade {
  padding: 0.5rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  background: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  transition: all 0.2s;
}

.btn-grade:hover {
  background: #f8fafc;
}

.btn-grade.active {
  background: #3b82f6;
  color: white;
  border-color: #3b82f6;
}

.comment-section label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #374151;
}

.comment-section textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  resize: vertical;
  font-family: inherit;
}

.feedback-section {
  margin: 2rem 0;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 0.5rem;
}

.feedback-section label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #374151;
}

.feedback-section textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  resize: vertical;
  font-family: inherit;
}

.review-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}

.btn-save,
.btn-finalize {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}

.btn-save {
  background: #f3f4f6;
  color: #374151;
}

.btn-save:hover:not(:disabled) {
  background: #e5e7eb;
}

.btn-finalize {
  background: #16a34a;
  color: white;
}

.btn-finalize:hover:not(:disabled) {
  background: #15803d;
}

.btn-save:disabled,
.btn-finalize:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .review-header {
    flex-direction: column;
    gap: 1rem;
  }

  .score-info .score-display {
    text-align: left;
  }

  .answer-comparison {
    grid-template-columns: 1fr;
  }

  .review-actions {
    flex-direction: column;
  }
}
</style>