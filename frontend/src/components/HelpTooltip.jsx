import { Tooltip, IconButton } from "@mui/material";
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";

const HelpTooltip = () => {
  return (
    <Tooltip title="Select a model, adjust settings if needed, then submit." arrow>
      <IconButton>
        <InfoOutlinedIcon />
      </IconButton>
    </Tooltip>
  );
};

export default HelpTooltip;
