import { Button, Box } from '@mui/material';

const SubmitButton = ({ onClick }) => (
  <Box sx={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
    <Button
      onClick={onClick}
      variant="contained"
      color="secondary"
      sx={{
        height: "48px",          // Match input field height
        ml: 2,                   // Add some margin to separate from the text field
        padding: "12px 24px",
        fontSize: "16px",
        borderRadius: "500px",    // Optional: adds rounded corners
      }}
    >
      Submit
    </Button>
  </Box>
);

export default SubmitButton;
