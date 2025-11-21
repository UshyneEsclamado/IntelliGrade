import { createClient } from '@supabase/supabase-js'

// Fixed the URL typo and added proper configuration
const supabaseUrl = 'https://yvkivgoloowsvmybxalu.supabase.co'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2a2l2Z29sb293c3ZteWJ4YWx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM1Mzk3ODQsImV4cCI6MjA3OTExNTc4NH0.u-dNx-K2GAFOh3VEEVPOaL9Y0dmpfb1m-1KLWZxG4hA'

export const supabase = createClient(supabaseUrl, supabaseKey, {
  auth: {
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: true
  },
  realtime: {
    params: {
      eventsPerSecond: 2
    }
  }
})
