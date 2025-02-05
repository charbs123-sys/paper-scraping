import { TextField, Typography, Box } from '@mui/material';

const InputField = ({ text, setText }) => {
  const maxLength = 1000;

  const handleChange = (e) => {
    if (e.target.value.length <= maxLength) {
      setText(e.target.value); // Update the text state in the parent
    }
  };

  return (
    <Box sx={{ position: 'relative', width: '55%', margin: '0 auto', mt: 4 }}>
      <TextField
        value={text}
        onChange={handleChange}
        placeholder="Type a short summary..."
        variant="outlined"
        multiline
        rows={12}
        fullWidth
        sx={{
          '& .MuiInputBase-root': {
            position: 'relative',
          },
          '& .MuiOutlinedInput-root': {
            paddingBottom: 0,
          },
          '& .MuiInputBase-input': {
            fontSize: '18px',
          },
        }}
      />
      <Typography 
        variant="body2" 
        color="textSecondary" 
        sx={{
          position: 'absolute', 
          bottom: 10,
          right: 14,
          fontSize: '14px',
        }}
      >
        {text.length}/{maxLength}
      </Typography>
    </Box>
  );
};

export default InputField;
