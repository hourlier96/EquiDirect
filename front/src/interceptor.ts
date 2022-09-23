import axiosInstance from "./helpers/axios"

const setup = (store) => {
    axiosInstance.axiosInstance.interceptors.request.use(
    (config) => {
        const token = "TODO" //call token
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