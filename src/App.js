import React from "react";
import "./App.css";
import { Container, Typography, Box } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Card from "./elements/card";
import ButtonAppBar from "./elements/appbar";

function App() {
  return (
    <div>
      <ButtonAppBar />
      <Container maxWidth="md">
        <Typography
          component="div"
          style={{ backgroundColor: "#ecf6ff", height: "100vh" }}
        >
          <Box component="span" m={1}>
            <Grid
              container
              spacing={1}
              direction="column"
              justify="flex-start"
              alignItems="left"
            >
              <Grid item xs={12}>
                <Card
                  timestamp={"1587946936"}
                  type={"error"}
                  keyText={"Sample Error Key Text"}
                  valText={"This is an error message"}
                />
              </Grid>
              <Grid item xs={12}>
                <Card
                  timestamp={"1587946936"}
                  type={"warning"}
                  keyText={"Sample Warning Key Text"}
                  valText={"This is a warning message"}
                />
              </Grid>
              <Grid item xs={12}>
                <Card
                  timestamp={"1587946936"}
                  type={"alert"}
                  keyText={"Sample Alert Key Text"}
                  valText={"This is an alert message"}
                />
              </Grid>
              <Grid item xs={12}>
                <Card
                  timestamp={"1587946936"}
                  type={"debug"}
                  keyText={"Sample Debug Key Text"}
                  valText={"This is a debug message"}
                />
              </Grid>
            </Grid>
          </Box>
        </Typography>
      </Container>
    </div>
  );
}

export default App;
