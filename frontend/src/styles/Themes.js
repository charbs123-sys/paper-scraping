import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: 'rgb(0, 0, 0)',
    },
    secondary: {
      main: 'rgb(255, 0, 0)',
    },
    background: {
      default:'rgba(214, 218, 221, 0.57)',
    },
  },
  typography: {
    fontFamily: 'Roboto, Arial, sans-serif',
  },
});

export default theme;
