import { useState } from "react";
import { Box } from "@mui/material";
import Title from "./Title";
import ModelOptions from "./ModelToggle";
import InputField from "./InputField";
import SubmitButton from "./SubmitButton";

const MainComponent = () => {
  const [text, setText] = useState("");

  return (
    <Box sx={{ width: "60%", margin: "20px auto", position: "relative" }}>
      <Title />
      <ModelOptions /> 
      <InputField text={text} setText={setText} />
      <SubmitButton sx={{ position: "absolute", bottom: 10, right: 0 }} />
    </Box>
  );
};

export default MainComponent;
