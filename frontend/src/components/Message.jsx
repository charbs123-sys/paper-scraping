import { Typography, Box, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const Message = ({ message }) => {
  if (!Array.isArray(message)) {
    return (
      <Typography variant="h6" align="center" color="error" sx={{ mt: 4 }}>
        Error: Failed to retrieve recommendations.
      </Typography>
    );
  }

  if (message.length === 0) {
    return (
      <Typography variant="h6" align="center" color="textSecondary" sx={{ mt: 4 }}>
        No recommendations yet.
      </Typography>
    );
  }

  return (
    <Box sx={{ width: '80%', margin: '20px auto', textAlign: 'center' }}>
      <TableContainer component={Paper} elevation={3} sx={{ border: '2px solid #1976d2' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: 'bold', border: '2px solid #1976d2', textAlign: 'center' }}>#</TableCell>
              <TableCell sx={{ fontWeight: 'bold', border: '2px solid #1976d2', textAlign: 'center' }}>Title</TableCell>
              <TableCell sx={{ fontWeight: 'bold', border: '2px solid #1976d2', textAlign: 'center' }}>Summary</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {message.map((item, index) => (
              <TableRow key={index}>
                <TableCell sx={{ border: '2px solid #1976d2', textAlign: 'center' }}>{index + 1}</TableCell>
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
