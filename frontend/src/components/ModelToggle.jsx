import { Box, FormControl, FormControlLabel, Radio, RadioGroup, Typography } from "@mui/material";

const ModelOptions = ({ model, setModel, option, setOption }) => {
  return (
    <Box sx={{ width: "100%", mb: 2, textAlign: "center" }}>
      <FormControl component="fieldset">
        <Typography variant="h6" sx={{ mb: 1 }}>Select Model</Typography>
        <RadioGroup
          row
          value={model}
          onChange={(e) => setModel(e.target.value)}
          sx={{ justifyContent: "center" }}  // Center the model options
        >
          <FormControlLabel value="model1" control={<Radio />} label="TF-IDF" />
          <FormControlLabel value="model2" control={<Radio />} label="Doc2Vec" />
        </RadioGroup>

        {model === "model2" && (
          <Box sx={{ mt: 2 }}>
            <RadioGroup
              row
              value={option}
              onChange={(e) => setOption(parseInt(e.target.value, 10))}
              sx={{ justifyContent: "center" }}  // Center the radio buttons
            >
              <FormControlLabel value={0} control={<Radio />} label="dm = 0" />
              <FormControlLabel value={1} control={<Radio />} label="dm = 1" />
            </RadioGroup>
          </Box>
        )}
      </FormControl>
    </Box>
  );
};

export default ModelOptions;
