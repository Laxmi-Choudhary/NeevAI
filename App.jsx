import React, { useState, useEffect, lazy, Suspense } from 'react';
import { useTranslation } from 'react-i18next';
import { safeLogEvent } from './firebase';
import { AuthProvider } from './context/AuthContext';
import Header from './components/Header';
import Hero from './components/Hero';
import './i18n';

// Lazy loaded components
const Timeline = lazy(() => import('./components/Timeline'));
const ChatPanel = lazy(() => import('./components/ChatPanel'));
const EligibilityWizard = lazy(() => import('./components/EligibilityWizard'));
const QuizSection = lazy(() => import('./components/QuizSection'));
const ResourcesSection = lazy(() => import('./components/ResourcesSection'));

const LoadingFallback = () => (
  <div className="w-full h-48 flex items-center justify-center">
    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-saffron"></div>
  </div>
);

function App() {
  const { t } = useTranslation();
  const [language, setLanguage] = useState('en');

  useEffect(() => {
    safeLogEvent('page_view', { page_title: 'Home' });
  }, []);

  return (
    <AuthProvider>
      <div className="min-h-screen bg-bglight flex flex-col relative selection:bg-saffron/30">
        <Header language={language} setLanguage={setLanguage} />
        
        <main id="main-content" className="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-12 space-y-24 outline-none">
          <section id="hero" data-testid="section-hero">
            <Hero />
          </section>

          <Suspense fallback={<LoadingFallback />}>
            <section id="timeline" data-testid="section-timeline">
              <h2 className="text-4xl font-cabinet font-bold text-navy mb-8 text-center">{t('nav_timeline')}</h2>
              <Timeline />
            </section>

            <section id="eligibility" data-testid="section-eligibility">
              <h2 className="text-4xl font-cabinet font-bold text-navy mb-8 text-center">{t('nav_eligibility')}</h2>
              <EligibilityWizard />
            </section>

            <section id="quiz" data-testid="section-quiz">
              <h2 className="text-4xl font-cabinet font-bold text-navy mb-8 text-center">{t('nav_quiz')}</h2>
              <QuizSection />
            </section>

            <section id="chat" data-testid="section-chat">
              <h2 className="text-4xl font-cabinet font-bold text-navy mb-8 text-center">{t('nav_chat')}</h2>
              <div className="max-w-3xl mx-auto">
                <ChatPanel language={language} />
              </div>
            </section>

            <section id="resources" data-testid="section-resources">
              <h2 className="text-4xl font-cabinet font-bold text-navy mb-8 text-center">{t('nav_resources')}</h2>
              <ResourcesSection />
            </section>
          </Suspense>
        </main>

        <footer className="bg-navy py-12 text-center text-white/70 border-t border-white/10">
          <p className="font-ibm">
            {t('app_name')} &copy; {new Date().getFullYear()} - {t('footer_text')}
          </p>
        </footer>
      </div>
    </AuthProvider>
  );
}

export default App;

