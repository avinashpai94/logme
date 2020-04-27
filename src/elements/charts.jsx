import React from "react";
import Grid from "@material-ui/core/Grid";
import InfoIcon from "@material-ui/icons/Info"; //Debug
import NotificationsIcon from "@material-ui/icons/Notifications"; //Alert
import WarningIcon from "@material-ui/icons/Warning"; //Warning
import CancelIcon from "@material-ui/icons/Cancel"; //Error
import { red, yellow, green, grey } from "@material-ui/core/colors";
import Typography from "@material-ui/core/Typography";
import { withStyles } from "@material-ui/core/styles";
import PropTypes from "prop-types";

const useStyles = (theme) => ({
  error: {
    color: red[900],
  },
  warning: {
    color: yellow[500],
  },
  alert: {
    color: green[500],
  },
  debug: {
    color: grey[500],
  },
});

class Charts extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      errors: props.errors,
      warnings: props.warnings,
      alerts: props.alerts,
      debugs: props.debugs,
    };
  }
  render() {
    const { classes } = this.props;
    return (
      <Grid container direction="row" justify="center" alignItems="center">
        <Typography
          variant="h2"
          className={classes.error}
          style={{ padding: "20px" }}
        >
          <CancelIcon fontSize="large"></CancelIcon>
          {this.state.errors}
        </Typography>
        <Typography
          variant="h2"
          className={classes.warning}
          style={{ padding: "20px" }}
        >
          <WarningIcon fontSize="large"></WarningIcon>
          {this.state.warnings}
        </Typography>
        <Typography
          variant="h2"
          className={classes.alert}
          style={{ padding: "20px" }}
        >
          <NotificationsIcon fontSize="large"></NotificationsIcon>
          {this.state.alerts}
        </Typography>
        <Typography
          variant="h2"
          className={classes.debug}
          style={{ padding: "20px" }}
        >
          <InfoIcon fontSize="large"></InfoIcon>
          {this.state.debugs}
        </Typography>
      </Grid>
    );
  }
}

Charts.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(useStyles)(Charts);
