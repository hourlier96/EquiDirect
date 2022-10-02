import axios from "axios";
import { APISettings } from "@/api/config";

const axiosInstance = axios.create(APISettings);

export default {
  axiosInstance,
  async get(entity, params, headers = null) {
    let config = {
      method: "GET",
      url: `/${entity}/`,
      params: params,
    };
    if (headers) {
      config["headers"] = headers;
    }
    return await axiosInstance(config);
  },
  async post(entity, payload) {
    return await axiosInstance({
      method: "POST",
      url: `/${entity}/`,
      data: payload,
    });
  },
  async put(entity, id, payload, headers = null) {
    let config = { method: "PUT", url: `/${entity}/${id}`, data: payload };
    if (headers) {
      config["headers"] = headers;
    }
    return await axiosInstance(config);
  },
  async delete(entity, id) {
    return await axiosInstance({
      method: "DELETE",
      url: `/${entity}/${id}`,
    });
  },
};
