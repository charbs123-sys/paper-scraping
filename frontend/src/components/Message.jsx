import { Typography, Box, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const Message = ({ message }) => {
  if (!message || message.length === 0) {
    return (
      <Typography variant="h6" align="center" color="textSecondary" sx={{ mt: 4 }}>
        No recommendations yet.
      </Typography>
    );
  }

  return (
    <Box sx={{ width: '80%', margin: '20px auto' }}>
      <TableContainer component={Paper} elevation={3} sx={{ border: '2px solid #1976d2' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: 'bold', border: '2px solid #1976d2' }}>#</TableCell>
              <TableCell sx={{ fontWeight: 'bold', border: '2px solid #1976d2' }}>Title</TableCell>
              <TableCell sx={{ fontWeight: 'bold', border: '2px solid #1976d2' }}>Summary</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {message.map((item, index) => (
              <TableRow key={index}>
                <TableCell sx={{ border: '2px solid #1976d2' }}>{index + 1}</TableCell>
                <TableCell sx={{ border: '2px solid #1976d2' }}>{item.title}</TableCell>
                <TableCell sx={{ border: '2px solid #1976d2' }}>{item.summary}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Message;
