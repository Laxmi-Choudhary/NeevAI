export const API_BASE = "/api";

export const ENDPOINTS = {
  TIMELINE: `${API_BASE}/timeline`,
  QUIZ: `${API_BASE}/quiz`,
  QUIZ_SUBMIT: `${API_BASE}/quiz/submit`,
  ELIGIBILITY: `${API_BASE}/eligibility/check`,
  CHAT: `${API_BASE}/chat`,
  BOOTH: `${API_BASE}/booth`,
  CALENDAR: `${API_BASE}/calendar/events`,
  VIDEOS: `${API_BASE}/videos`,
};


export const LANGUAGES = [
  { code: 'en', label: 'English' },
  { code: 'hi', label: 'हिंदी' },
  { code: 'ta', label: 'தமிழ்' },
  { code: 'bn', label: 'বাংলা' },
  { code: 'te', label: 'తెలుగు' },
];

export const CACHE_TTL = 5 * 60 * 1000; // 5 minutes in ms
