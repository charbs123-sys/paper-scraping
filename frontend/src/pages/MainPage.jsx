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
    try {
      const response = await axios.get('http://localhost:5000/recommendations', {
        params: { query: text }
      });
      setMessage(response.data.results);
      setText("");
    } catch (error) {
      console.error("Error retrieving papers:", error);
      setMessage("Failed to retrieve papers.");
    }
  };
  

  return (
    <div>
      <Title />
        <InputField value={text} onChange={(e) => setText(e.target.value)} />
        <SubmitButton onClick={handleSubmit} />
      <Message message={message} />
    </div>
  );
}

export default MainPage;
