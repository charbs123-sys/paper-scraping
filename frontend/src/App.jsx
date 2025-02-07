import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import theme from './styles/Themes';
import "./index.css";
import MainPage from "./pages/MainPage";
import { CssBaseline } from '@mui/material';

const AppContent = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline /> {/* This ensures the background color from the theme is applied */}
      <Router>
        <Routes>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
};

const App = () => {
  return <AppContent />;
};

export default App;
