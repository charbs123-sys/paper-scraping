import { Typography } from '@mui/material';

const Message = ({ message }) => (
  message && <Typography
    variant="body1"
    color="success.main"
    sx={{
      textAlign: 'center',
      marginTop: '95px',
      fontSize: '32px',
    }}
  >
    {message}
  </Typography>
);

export default Message;
