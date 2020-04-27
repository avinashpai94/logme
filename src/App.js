import React from "react";
import "./App.css";
import { Container, Typography, Box } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Card from "./elements/card";
import ButtonAppBar from "./elements/appbar";
import response from "./elements/logs.json";
import Charts from "./elements/charts";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: response.map(function (item) {
        return {
          timestamp: item.timestamp,
          accesstoken: item.accesstoken,
          type: item.type,
          key: item.key,
          text: item.text,
        };
      }),
    };
  }
  render() {
    this.state.data.reverse();
    return (
      <div style={{ backgroundColor: "#ecf6ff" }}>
        <ButtonAppBar style={{ height: "10vh" }} />

        <Container maxWidth="xl">
          <Typography
            component="div"
            style={{ backgroundColor: "#ecf6ff", height: "35vh" }}
          ></Typography>
          <Charts
            errors={
              this.state.data.filter((item) => item.type === "error").length
            }
            warnings={
              this.state.data.filter((item) => item.type === "warning").length
            }
            alerts={
              this.state.data.filter((item) => item.type === "alert").length
            }
            debugs={
              this.state.data.filter((item) => item.type === "debug").length
            }
          ></Charts>
        </Container>
        <Container maxWidth="lg">
          <Typography
            component="div"
            style={{
              backgroundColor: "#ecf6ff",
              height: "45vh",
              overflowY: "auto",
              overflowX: "hidden",
              padding: "5px",
            }}
          >
            <Box component="span" m={1}>
              <Grid
                container
                spacing={1}
                direction="column"
                justify="flex-start"
                alignItems="left"
              >
                <ul style={{ listStyleType: "none" }}>
                  {this.state.data.map((item, key) => {
                    return (
                      <li style={{ margin: "5px 0" }} key={key}>
                        <Grid item xs={12}>
                          <Card
                            timestamp={item.timestamp}
                            type={item.type}
                            keyText={item.key}
                            valText={item.text}
                          />
                        </Grid>
                      </li>
                    );
                  })}
                </ul>
              </Grid>
            </Box>
          </Typography>
        </Container>
      </div>
    );
  }
}

export default App;
