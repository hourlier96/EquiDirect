import { APISettings } from "../config.js";
import axios from "axios";
export default {
  getUserFromEmail(email, callback) {
    return axios({
      method: "GET",
      url: APISettings.baseURL + "/users/",
      params: {
        email: email,
      },
    })
      .then(
        function (response) {
          callback(response.data);
        }.bind(this)
      )
      .catch(
        function (error) {
          callback(error);
        }.bind(this)
      );
  },
};
