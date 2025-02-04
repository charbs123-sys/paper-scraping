import { useState } from "react";
import axios from 'axios';
import Title from '../components/Title';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import Message from '../components/Message';

const MainPage = () => {
  const [text, setText] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async () => {
    console.log("Submit clicked, query:", text);

    if (!text) {
      console.error("Query is empty");
      setMessage("Please enter a query.");
      return;
    }

    try {
      const response = await axios.get('http://localhost:5000/recommendations', {
        params: { query: text }
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
      <InputField text={text} setText={setText} /> {/* Pass text and setText to InputField */}
      <SubmitButton onClick={handleSubmit} />
      <Message message={message} />
    </div>
  );
}

export default MainPage;
