import { TextField, Typography, Box } from '@mui/material';

const InputField = ({ text, setText }) => {
  const maxLength = 1000;

  const handleChange = (e) => {
    if (e.target.value.length <= maxLength) {
      setText(e.target.value);
    }
  };

  return (
    <Box sx={{ position: 'relative', width: '60%', mt: 2 }}>
      <TextField
        value={text}
        onChange={handleChange}
        placeholder="Type a short summary..."
        variant="outlined"
        multiline
        rows={12}
        fullWidth
        sx={{
          '& .MuiOutlinedInput-root': {
            '& fieldset': {
              borderColor: '#000', // Darker outline color
              borderWidth: '2px', // Thicker outline
            },
            '&:hover fieldset': {
              borderColor: '#333', // Slightly lighter on hover
            },
            '&.Mui-focused fieldset': {
              borderColor:'rgb(0, 128, 255)', // Highlight color when focused
              borderWidth: '3px', // Even thicker when focused
            },
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
