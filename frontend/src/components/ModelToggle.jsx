import { Box, FormControl, FormControlLabel, Radio, RadioGroup, Typography, Tooltip } from "@mui/material";

const ModelOptions = ({ model, setModel, option, setOption }) => {
  return (
    <Box sx={{ width: "100%", mb: 2, textAlign: "center", position: "relative" }}>
      <FormControl component="fieldset">
        <Typography variant="h6" sx={{ mb: 1 }}>Select Model</Typography>

        <RadioGroup
          row
          value={model}
          onChange={(e) => setModel(e.target.value)}
          sx={{ justifyContent: "center" }}  // Center the model options
        >
          <Tooltip title="TF-IDF: Traditional keyword-based summarization" arrow>
            <FormControlLabel value="model1" control={<Radio />} label="TF-IDF" />
          </Tooltip>

          <Tooltip title="Doc2Vec: Contextual vector-based summarization" arrow>
            <FormControlLabel value="model2" control={<Radio />} label="Doc2Vec" />
          </Tooltip>
        </RadioGroup>

        {model === "model2" && (
          <Box sx={{ mt: 2 }}>
            <RadioGroup
              row
              value={option}
              onChange={(e) => setOption(parseInt(e.target.value, 10))}
              sx={{ justifyContent: "center" }}  // Center the radio buttons
            >
              <Tooltip title="dm = 0: Distributed Bag of Words (DBOW) mode" arrow>
                <FormControlLabel value={0} control={<Radio />} label="dm = 0" />
              </Tooltip>

              <Tooltip title="dm = 1: Distributed Memory (DM) mode" arrow>
                <FormControlLabel value={1} control={<Radio />} label="dm = 1" />
              </Tooltip>
            </RadioGroup>
          </Box>
        )}
      </FormControl>
    </Box>
  );
};

export default ModelOptions;
