import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import InfoIcon from "@material-ui/icons/Info"; //Debug
import NotificationsIcon from "@material-ui/icons/Notifications"; //Alert
import WarningIcon from "@material-ui/icons/Warning"; //Warning
import CancelIcon from "@material-ui/icons/Cancel"; //Error
import { red, yellow, green, grey } from "@material-ui/core/colors";

const iconRender = (type) => {
  if (type === "error") {
    return [
      <CancelIcon fontSize="small" style={{ color: red[900] }} />,
      red[100],
    ];
  } else if (type === "warning") {
    return [
      <WarningIcon fontSize="small" style={{ color: yellow[500] }} />,
      yellow[100],
    ];
  } else if (type === "alert") {
    return [
      <NotificationsIcon fontSize="small" style={{ color: green[500] }} />,
      green[100],
    ];
  } else {
    return [
      <InfoIcon fontSize="small" style={{ color: grey[500] }} />,
      grey[100],
    ];
  }
};

const useStyles = makeStyles((theme) => ({
  root: {
    width: "auto",
    display: "block",
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
  timestamp: {
    marginLeft: "auto",
    marginRight: 0,
  },
}));

function timeConverter(UNIX_timestamp) {
  var a = new Date(UNIX_timestamp * 1000);
  var months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time =
    hour + ":" + min + ":" + sec + " " + date + " " + month + " " + year;
  return time;
}

const Card = (props) => {
  let { timestamp, type, keyText, valText } = props;
  const classes = useStyles();
  let timeText = timeConverter(timestamp);
  let [icon, bgcolor] = iconRender(type);
  return (
    <div className={classes.root}>
      <ExpansionPanel style={{ backgroundColor: bgcolor }}>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography p={1} className={classes.heading}>
            {icon}
          </Typography>
          <Typography p={1} className={classes.heading}>
            {keyText}
          </Typography>
          <Typography p={1} className={classes.timestamp}>
            {timeText}
          </Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography>{valText}</Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
    </div>
  );
};

export default Card;
