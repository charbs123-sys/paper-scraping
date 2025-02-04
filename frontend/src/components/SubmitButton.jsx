import { Button } from '@mui/material';

const SubmitButton = ({ onClick }) => (
  <Button
    onClick={onClick}
    variant="contained"
    color="secondary"
    sx={{
      position: 'relative',     // Keeps the button fixed in the viewport
      bottom: '175px',        // Positions it 20px from the bottom
      left: '1500px',         // Positions it 20px from the right
      padding: '12px 24px',
      fontSize: '16px',
      borderRadius: '500px',   // Optional: adds rounded corners
    }}
  >
    Submit
  </Button>
);

export default SubmitButton;
