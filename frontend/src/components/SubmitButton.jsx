import { Button } from '@mui/material';

const SubmitButton = ({ onClick }) => (
  <Button
    onClick={onClick}
    variant="contained"
    color="secondary"
    sx={{
      position: 'fixed',  // Change to fixed
      top: '53%',         // Adjust vertical positioning (can use px or %)
      left: '50%',        // Center horizontally
      transform: 'translateX(-50%)',  // Ensure it's centered horizontally
      padding: '12px 24px',
      fontSize: '16px',
      zIndex: 999,        // Ensures it stays on top of other elements
    }}
  >
    Submit
  </Button>
);

export default SubmitButton;
