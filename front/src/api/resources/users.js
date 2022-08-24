import { APISettings } from "../config.js";

export default {
  index() {
    return fetch(APISettings.baseURL + "/users/", {
      method: "GET",
      headers: APISettings.headers,
    })
      .then(function (response) {
        if (response.status != 200) {
          throw response.status;
        } else {
          return response.json();
        }
      })
      .then(function (data) {
        console.log(data);
      });
  },

  store(data) {},
};
