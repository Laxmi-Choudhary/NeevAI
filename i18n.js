import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      "app_name": "NeevAI",
      "nav_timeline": "Timeline",
      "nav_eligibility": "Eligibility",
      "nav_quiz": "Quiz",
      "nav_chat": "AI Expert",
      "nav_resources": "Resources",
      "hero_title": "Empowering Every Voter",
      "hero_subtitle": "Your AI-powered guide to the Indian Electoral Process.",
      "skip_to_content": "Skip to content",
      "footer_text": "Election Process Education Assistant"
    }
  },
  hi: {
    translation: {
      "app_name": "नींवAI",
      "nav_timeline": "समयरेखा",
      "nav_eligibility": "पात्रता",
      "nav_quiz": "प्रश्नोत्तरी",
      "nav_chat": "AI विशेषज्ञ",
      "nav_resources": "संसाधन",
      "hero_title": "हर मतदाता को सशक्त बनाना",
      "hero_subtitle": "भारतीय चुनावी प्रक्रिया के लिए आपका AI-आधारित मार्गदर्शक।",
      "skip_to_content": "सामग्री पर जाएँ",
      "footer_text": "चुनाव प्रक्रिया शिक्षा सहायक"
    }
  },
  // Adding placeholders for others
  ta: { translation: { "app_name": "நீவ்AI" } },
  bn: { translation: { "app_name": "নীভAI" } },
  te: { translation: { "app_name": "నీవ్AI" } }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
