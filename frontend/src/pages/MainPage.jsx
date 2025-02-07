import { useState } from "react";
import axios from "axios";
import Title from "../components/Title";
import InputField from "../components/InputField";
import SubmitButton from "../components/SubmitButton";
import Message from "../components/Message";
import ModelToggle from "../components/ModelToggle";
import HelpTooltip from "../components/HelpTooltip";
import { Box } from "@mui/material";

const MainPage = () => {
  const [text, setText] = useState("");
  const [message, setMessage] = useState("");
  const [model, setModel] = useState("model1");
  const [option, setOption] = useState(0);

  const handleSubmit = async () => {
    console.log("Submit clicked, query:", text, "Model:", model, "Option:", option);

    if (!text) {
      console.error("Query is empty");
      setMessage("Please enter a query.");
      return;
    }

    try {
      const response = await axios.get("http://localhost:5000/recommendations", {
        params: { query: text, model, option },
      });
      console.log("Response data:", response.data);
      setMessage(response.data.results);
    } catch (error) {
      console.error("Error retrieving papers:", error);
      setMessage("Failed to retrieve papers.");
    }
  };

  return (
    <div>
      <Title />
      <ModelToggle model={model} setModel={setModel} option={option} setOption={setOption} />
      <Box sx={{ display: "flex", justifyContent: "center", alignItems: "center", mt: 4 }}>
        <InputField text={text} setText={setText} />
        <HelpTooltip /> 
        <SubmitButton onClick={handleSubmit} />
      </Box>

      <Message message={message} />
    </div>
  );
};

export default MainPage;
