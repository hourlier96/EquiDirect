import axiosInstance from "./helpers/axios"
import { authStore } from "./stores/auth";

const setup = () => {
    axiosInstance.axiosInstance.interceptors.request.use(
    (config) => {
        const store = authStore();
        const token = store.accessToken
        if (config.headers) {
            config.headers["Authorization"] = `Bearer ${token}`
            return config;
        }
    },
    (error) => {
        return Promise.reject(error);
    }
  );
}

export default setup;