<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <!-- Educational floating elements -->
      <div class="floating-element element-1">
        <svg width="35" height="35" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-2">
        <svg width="33" height="33" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-3">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-4">
        <svg width="38" height="38" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-5">
        <svg width="33" height="33" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M20,8L12,13L4,8V6L12,11L20,6M20,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6C22,5.89 21.1,4 20,4Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-6">
        <svg width="36" height="36" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
        </svg>
      </div>
    </div>
    
    <div class="verification-container">
      <!-- Loading State -->
      <div v-if="isLoading" class="verification-box loading-state">
        <div class="logo-section">
          <div class="logo-image-container">
            <img 
              src="@/assets/New IntelliGrade Logo Way BG 3.png"
              alt="IntelliGrade Logo" 
              class="logo-image"
            />
          </div>
        </div>
        
        <div class="status-icon loading-icon">
          <div class="loading-spinner"></div>
        </div>
        
        <h1 class="verification-title">Verifying Your Email</h1>
        <p class="verification-subtitle">Please wait while we confirm your account...</p>
      </div>

      <!-- Success State -->
      <div v-else-if="verified" class="verification-box success-state">
        <div class="logo-section">
          <div class="logo-image-container">
            <img 
              src="@/assets/New IntelliGrade Logo Way BG 3.png"
              alt="IntelliGrade Logo" 
              class="logo-image"
            />
          </div>
        </div>
        
        <div class="status-icon success-icon">
          <svg width="60" height="60" viewBox="0 0 24 24" fill="#22c55e">
            <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M11,16.5L18,9.5L16.59,8.09L11,13.67L7.41,10.09L6,11.5L11,16.5Z"/>
          </svg>
        </div>
        
        <h1 class="verification-title success-title">Email Verified Successfully!</h1>
        <p class="verification-subtitle">Welcome to IntelliGrade! Your {{ userRole }} account has been confirmed and you're ready to start.</p>
        
        <div class="action-buttons">
          <button @click="goToDashboard" class="primary-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10,17V14H3V10H10V7L15,12L10,17M10,2H19A2,2 0 0,1 21,4V20A2,2 0 0,1 19,22H10A2,2 0 0,1 8,20V18H10V20H19V4H10V6H8V4A2,2 0 0,1 10,2Z"/>
            </svg>
            Go to {{ userRole === 'teacher' ? 'Teacher Dashboard' : 'Student Dashboard' }}
          </button>
        </div>
      </div>

      <!-- Error State -->
      <div v-else class="verification-box error-state">
        <div class="logo-section">
          <div class="logo-image-container">
            <img 
              src="@/assets/New IntelliGrade Logo Way BG 3.png"
              alt="IntelliGrade Logo" 
              class="logo-image"
            />
          </div>
        </div>
        
        <div class="status-icon error-icon">
          <svg width="60" height="60" viewBox="0 0 24 24" fill="#ef4444">
            <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,6A2,2 0 0,1 14,8A2,2 0 0,1 12,10A2,2 0 0,1 10,8A2,2 0 0,1 12,6M12,12A2,2 0 0,1 14,14A2,2 0 0,1 12,16A2,2 0 0,1 10,14A2,2 0 0,1 12,12Z"/>
          </svg>
        </div>
        
        <h1 class="verification-title error-title">Verification Failed</h1>
        <p class="verification-subtitle">{{ error || 'We couldn\'t verify your email address. The link may be invalid or expired.' }}</p>
        
        <div class="action-buttons">
          <router-link to="/signup" class="primary-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z"/>
            </svg>
            Try Again
          </router-link>
          <router-link to="/login" class="secondary-btn">
            Already have an account?
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { supabase } from '../supabase.js';

export default {
  name: 'EmailVerified',
  data() {
    return {
      isLoading: true,
      verified: false,
      error: null,
      userRole: 'teacher'
    }
  },
  async mounted() {
    console.log('=== EMAIL VERIFICATION STARTED ===');
    console.log('Full URL:', window.location.href);
    console.log('URL Search params:', window.location.search);
    console.log('URL Hash:', window.location.hash);
    
    // Check if user is already logged in first
    await this.checkExistingSession();
    
    // If not logged in, try to process verification
    if (!this.verified) {
      setTimeout(async () => {
        await this.handleEmailVerification();
      }, 500);
    }
  },
  methods: {
    async checkExistingSession() {
      try {
        console.log('=== CHECKING EXISTING SESSION ===');
        const { data: { session }, error } = await supabase.auth.getSession();
        
        if (!error && session?.user) {
          console.log('✅ Found existing session!');
          console.log('User:', session.user.email);
          console.log('Email confirmed at:', session.user.email_confirmed_at);
          
          // Check if email is already verified
          if (session.user.email_confirmed_at) {
            await this.handleVerificationSuccess(session.user, session);
            return true;
          }
        }
        
        console.log('No existing session found');
        return false;
      } catch (error) {
        console.error('Error checking session:', error);
        return false;
      }
    },

    async handleEmailVerification() {
      try {
        console.log('=== PROCESSING URL PARAMETERS ===');
        
        const urlHash = window.location.hash;
        const urlSearch = window.location.search;
        
        console.log('URL Hash:', urlHash);
        console.log('URL Search:', urlSearch);

        // If no parameters at all, show helpful error
        if (!urlHash && !urlSearch) {
          throw new Error('No verification parameters found. Please use the verification link from your email.');
        }

        let params = {};
        
        // Parse hash parameters (Supabase auth often uses fragments)
        if (urlHash) {
          const hashString = urlHash.substring(1); // Remove #
          console.log('Hash string:', hashString);
          
          // Handle both URLSearchParams format and manual parsing
          try {
            const hashParams = new URLSearchParams(hashString);
            for (const [key, value] of hashParams) {
              params[key] = value;
            }
          } catch (e) {
            // Manual parsing for complex hash formats
            const hashPairs = hashString.split('&');
            hashPairs.forEach(pair => {
              const [key, value] = pair.split('=');
              if (key && value) {
                params[decodeURIComponent(key)] = decodeURIComponent(value);
              }
            });
          }
        }

        // Parse search parameters
        if (urlSearch) {
          const searchParams = new URLSearchParams(urlSearch);
          for (const [key, value] of searchParams) {
            params[key] = value;
          }
        }

        console.log('Parsed parameters:', Object.keys(params).reduce((acc, key) => {
          acc[key] = key.includes('token') ? (params[key] ? 'Present' : 'Missing') : params[key];
          return acc;
        }, {}));

        // Extract tokens and type
        const token = params.access_token || params.token || params.confirmation_token || params.recovery_token;
        const refreshToken = params.refresh_token;
        const type = params.type || 'signup';
        const error_code = params.error;
        const error_description = params.error_description;

        // Handle errors in URL
        if (error_code) {
          throw new Error(`Authentication error: ${error_description || error_code}`);
        }

        if (!token) {
          throw new Error('No verification token found in URL. Please check your email for the correct verification link.');
        }

        console.log('Found token type:', type);
        console.log('Has refresh token:', !!refreshToken);

        // Try different verification methods
        await this.tryVerificationMethods(token, refreshToken, type, params);

      } catch (err) {
        console.error('❌ Email verification failed:', err);
        this.showError(err.message || 'Email verification failed');
      }
    },

    async tryVerificationMethods(token, refreshToken, type, allParams) {
      console.log('=== TRYING VERIFICATION METHODS ===');

      // Method 1: Set session with tokens (most reliable for email verification)
      if (token) {
        try {
          console.log('Method 1: Setting session with tokens...');
          
          const sessionData = {
            access_token: token,
            refresh_token: refreshToken || token // Some flows use the same token
          };
          
          const { data, error } = await supabase.auth.setSession(sessionData);

          if (!error && data?.session?.user) {
            console.log('✅ Method 1 successful - setSession worked!');
            await this.handleVerificationSuccess(data.session.user, data.session);
            return;
          }
          
          console.log('Method 1 failed:', error?.message);
          
          // Try with just access token
          if (refreshToken) {
            const { data: data2, error: error2 } = await supabase.auth.setSession({
              access_token: token,
              refresh_token: null
            });
            
            if (!error2 && data2?.session?.user) {
              console.log('✅ Method 1b successful - setSession with access token only!');
              await this.handleVerificationSuccess(data2.session.user, data2.session);
              return;
            }
            console.log('Method 1b failed:', error2?.message);
          }
          
        } catch (e) {
          console.log('Method 1 error:', e.message);
        }
      }

      // Method 2: Try exchangeCodeForSession for OAuth flows
      if (allParams.code) {
        try {
          console.log('Method 2: Exchange code for session...');
          
          const { data, error } = await supabase.auth.exchangeCodeForSession(allParams.code);
          
          if (!error && data?.session?.user) {
            console.log('✅ Method 2 successful!');
            await this.handleVerificationSuccess(data.session.user, data.session);
            return;
          }
          
          console.log('Method 2 failed:', error?.message);
        } catch (e) {
          console.log('Method 2 error:', e.message);
        }
      }

      // Method 3: Try various OTP verification methods
      const otpMethods = [
        { token_hash: token, type: 'email' },
        { token_hash: token, type: 'signup' },
        { token_hash: token, type: 'email_change' },
        { token_hash: token, type: 'recovery' },
        { token: token, type: 'email' },
        { token: token, type: 'signup' }
      ];

      for (let i = 0; i < otpMethods.length; i++) {
        try {
          console.log(`Method 3.${i + 1}: verifyOtp with`, otpMethods[i]);
          
          const { data, error } = await supabase.auth.verifyOtp(otpMethods[i]);
          
          if (!error && data?.user) {
            console.log(`✅ Method 3.${i + 1} successful!`);
            await this.handleVerificationSuccess(data.user, data.session);
            return;
          }
          
          console.log(`Method 3.${i + 1} failed:`, error?.message);
        } catch (methodError) {
          console.log(`Method 3.${i + 1} threw error:`, methodError?.message);
        }
      }

      // Method 4: Listen for auth state changes
      this.setupAuthListener();
    },

    setupAuthListener() {
      console.log('Method 4: Setting up auth state listener...');
      
      let hasResolved = false;
      const timeout = 15000; // 15 seconds
      
      const { data: { subscription } } = supabase.auth.onAuthStateChange(async (event, session) => {
        console.log('🔄 Auth state change:', event, !!session);
        
        if (hasResolved) return;
        
        if ((event === 'SIGNED_IN' || event === 'TOKEN_REFRESHED') && session?.user) {
          hasResolved = true;
          console.log('✅ Auth listener caught authentication!');
          await this.handleVerificationSuccess(session.user, session);
          subscription?.unsubscribe();
        } else if (event === 'SIGNED_OUT') {
          console.log('User signed out during verification');
        }
      });

      // Timeout
      setTimeout(() => {
        if (!hasResolved) {
          hasResolved = true;
          subscription?.unsubscribe();
          console.log('⏰ Auth listener timeout');
          this.showError('Verification timed out. The verification link may be invalid, expired, or already used. Please try registering again.');
        }
      }, timeout);
    },

    async handleVerificationSuccess(user, session) {
      console.log('=== HANDLING VERIFICATION SUCCESS ===');
      console.log('User ID:', user?.id);
      console.log('Email:', user?.email);
      console.log('Email confirmed:', user?.email_confirmed_at ? 'Yes' : 'No');
      console.log('Session exists:', !!session);
      
      try {
        // Get user role from metadata or profile
        await this.determineUserRole(user);

        // Try to create/update user profile (don't fail verification if this fails)
        try {
          await this.ensureUserProfile(user);
        } catch (profileError) {
          console.warn('Profile operation failed, but continuing with verification:', profileError);
        }

        // Mark as verified
        this.verified = true;
        this.isLoading = false;
        this.error = null;

        console.log('✅ Verification complete! User role:', this.userRole);

        // Auto redirect after 3 seconds
        setTimeout(() => {
          this.goToDashboard();
        }, 3000);

      } catch (error) {
        console.error('Error in verification success handler:', error);
        // Still mark as verified since the auth part worked
        this.verified = true;
        this.isLoading = false;
        
        setTimeout(() => {
          this.goToDashboard();
        }, 2000);
      }
    },

    async determineUserRole(user) {
      console.log('Determining user role...');
      
      // First check user metadata
      this.userRole = user?.user_metadata?.role || 
                     user?.app_metadata?.role;
      
      // If no role in metadata, check profile table
      if (!this.userRole) {
        try {
          const { data: profile } = await supabase
            .from('profiles')
            .select('role')
            .eq('id', user.id)
            .single();
          
          if (profile?.role) {
            this.userRole = profile.role;
          }
        } catch (e) {
          console.log('Could not fetch profile role:', e.message);
        }
      }
      
      // Default fallback based on email
      if (!this.userRole) {
        this.userRole = user?.email?.includes('teacher') ? 'teacher' : 'student';
      }
      
      console.log('Final user role:', this.userRole);
    },

    async ensureUserProfile(user) {
      console.log('Creating/updating user profile...');
      
      try {
        // Check if profile exists
        const { data: existingProfile, error: fetchError } = await supabase
          .from('profiles')
          .select('*')
          .eq('id', user.id)
          .single();

        if (fetchError && fetchError.code !== 'PGRST116') {
          throw fetchError;
        }

        if (existingProfile) {
          console.log('Profile exists, updating verification status...');
          
          const { error: updateError } = await supabase
            .from('profiles')
            .update({ 
              email_verified: true,
              updated_at: new Date().toISOString()
            })
            .eq('id', user.id);

          if (updateError) throw updateError;
          
          this.userRole = existingProfile.role || this.userRole;
        } else {
          console.log('Creating new profile...');
          
          const profileData = {
            id: user.id,
            auth_user_id: user.id,
            full_name: user.user_metadata?.full_name || 
                      user.user_metadata?.name || 
                      user.email?.split('@')[0] || '',
            email: user.email,
            role: this.userRole,
            email_verified: true,
            created_at: new Date().toISOString(),
            updated_at: new Date().toISOString()
          };

          // Add role-specific fields
          if (this.userRole === 'student') {
            profileData.student_id = user.user_metadata?.student_id || null;
            profileData.grade_level = user.user_metadata?.grade_level || null;
          }

          const { error: insertError } = await supabase
            .from('profiles')
            .insert([profileData]);

          if (insertError) throw insertError;
        }

        console.log('✅ Profile operation completed successfully');

      } catch (error) {
        console.error('Profile operation failed:', error);
        throw error;
      }
    },

    showError(message) {
      console.log('=== SHOWING ERROR ===');
      console.log('Error message:', message);
      
      this.error = message;
      this.isLoading = false;
      this.verified = false;
    },

    goToDashboard() {
      console.log('=== GOING TO DASHBOARD ===');
      console.log('User role:', this.userRole);
      
      const dashboardRoutes = {
        teacher: '/teacher/dashboard',
        student: '/student-dashboard'
      };

      const route = dashboardRoutes[this.userRole] || '/teacher/dashboard';
      console.log('Navigating to:', route);

      try {
        this.$router.push(route);
      } catch (routerError) {
        console.log('Router failed, using window.location');
        window.location.href = route;
      }
    }
  }
}
</script>

<style scoped>
* { 
  margin: 0; 
  padding: 0; 
  box-sizing: border-box; 
}

.auth-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: transparent !important;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
}

.geometric-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 50%, #FBFFE4 100%);
}

.geometric-shapes::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.08) 50%, transparent 52%) 0 0 / 60px 60px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.08) 50%, transparent 52%) 0 0 / 60px 60px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.12) 0, transparent 40px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.12) 0, transparent 60px);
  animation: moveBackground 30s linear infinite;
}

.floating-elements {
  position: fixed;
  inset: 0;
  z-index: 1;
  pointer-events: none;
}

.floating-element {
  position: absolute;
  animation: educationalFloat 15s ease-in-out infinite;
  opacity: 0.6;
  filter: drop-shadow(0 4px 12px rgba(74, 155, 142, 0.25));
}

.element-1 { top: 15%; left: 10%; animation-delay: 1s; }
.element-2 { top: 30%; right: 15%; animation-delay: 3s; }
.element-3 { bottom: 20%; left: 8%; animation-delay: 5s; }
.element-4 { top: 20%; right: 8%; animation-delay: 7s; }
.element-5 { bottom: 30%; right: 12%; animation-delay: 9s; }
.element-6 { top: 50%; left: 5%; animation-delay: 11s; }

.verification-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  z-index: 10;
  position: relative;
  padding: 2rem;
}

.verification-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 2.5rem;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 25px 50px rgba(61, 141, 122, 0.1),
    0 10px 30px rgba(0, 0, 0, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  width: 100%;
  max-width: 500px;
  text-align: center;
  position: relative;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logo-section {
  margin-bottom: 1.5rem;
}

.logo-image-container {
  width: 100px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.logo-image {
  width: 80px;
  height: 80px;
  object-fit: contain;
  animation: gentleFloat 6s ease-in-out infinite;
}

.status-icon {
  margin: 1.5rem 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-icon {
  margin: 2rem 0;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(61, 141, 122, 0.1);
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.success-icon svg, .error-icon svg {
  filter: drop-shadow(0 4px 20px rgba(0, 0, 0, 0.1));
  animation: scaleIn 0.5s ease-out;
}

.verification-title {
  color: #3D8D7A;
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  letter-spacing: -0.5px;
}

.success-title {
  color: #22c55e;
}

.error-title {
  color: #ef4444;
}

.verification-subtitle {
  color: rgba(61, 141, 122, 0.8);
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  max-width: 400px;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  width: 100%;
  max-width: 300px;
}

.primary-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(61, 141, 122, 0.2);
  border: none;
  cursor: pointer;
}

.primary-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.secondary-btn {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.85rem;
  padding: 0.5rem;
  transition: all 0.3s ease;
  border-radius: 6px;
}

.secondary-btn:hover {
  background: rgba(61, 141, 122, 0.05);
  color: #26796a;
}

/* Animations */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes scaleIn {
  0% { 
    transform: scale(0); 
    opacity: 0;
  }
  50% { 
    transform: scale(1.1); 
  }
  100% { 
    transform: scale(1); 
    opacity: 1;
  }
}

@keyframes educationalFloat {
  0%, 100% { 
    transform: translateY(0px) translateX(0px) rotate(0deg); 
    opacity: 0.6;
  }
  50% { 
    transform: translateY(-20px) translateX(10px) rotate(180deg); 
    opacity: 0.8;
  }
}

@keyframes moveBackground {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(-60px, -60px);
  }
}

@keyframes gentleFloat {
  0%, 100% {
    transform: translateY(0px) scale(1);
  }
  50% {
    transform: translateY(-10px) scale(1.02);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .verification-container {
    padding: 1rem;
  }
  
  .verification-box {
    padding: 2rem;
    max-width: 100%;
  }
  
  .verification-title {
    font-size: 1.5rem;
  }
  
  .verification-subtitle {
    font-size: 0.9rem;
  }
  
  .logo-image-container {
    width: 80px;
    height: 80px;
  }
  
  .logo-image {
    width: 60px;
    height: 60px;
  }
  
  .floating-element {
    display: none;
  }
}

@media (max-width: 480px) {
  .verification-box {
    padding: 1.5rem;
    border-radius: 15px;
  }
  
  .verification-title {
    font-size: 1.3rem;
  }
  
  .verification-subtitle {
    font-size: 0.85rem;
  }
  
  .primary-btn {
    padding: 0.7rem 1.2rem;
    font-size: 0.85rem;
  }
}
</style>