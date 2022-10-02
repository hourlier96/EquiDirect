import axiosInstance from "./helpers/axios";
import { authStore } from "./stores/auth";

const setup = () => {
  axiosInstance.axiosInstance.interceptors.request.use(
    (config) => {
      const store = authStore();
      // Send Bearer when user is connected
      if (store.accessToken) {
        const token = store.accessToken;
        if (config.headers) {
          config.headers["Authorization"] = `Bearer ${token}`;
          return config;
        }
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
};

export default setup;
