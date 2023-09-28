import React from "react";
import {
  useQuery,
  useMutation,
  useQueryClient,
  QueryClient,
} from "@tanstack/react-query";
import axios from "axios";
import dayjs from "dayjs";

export function getRequests() {
  return useQuery({
    queryKey: ["requests"],
    queryFn: async () => {
      const response = await axios.get("/api/request");
      return response;
    },
  });
}

export function getPendingRequests() {
  return useQuery({
    queryKey: ["requests", "pending"],
    queryFn: async () => {
      const response = await axios.get("/api/request", {
        params: {
          approved: "False",
        },
      });
      return response;
    },
  });
}

export function getApprovedRequests() {
  return useQuery({
    queryKey: ["requests", "approved"],
    queryFn: async () => {
      const response = await axios.get("/api/request", {
        params: {
          approved: "true",
        },
      });
      return response;
    },
  });
}

export function getRequestsByDate(startDate, endDate) {
  if (!dayjs.isDayjs(startDate) || !dayjs.isDayjs(endDate)) {
    throw new Error("Both startDate and endDate must be Day.js date objects.");
  }

  const formattedStartDate = startDate.format("YYYY-MM-DD HH:mm:ss.SSSSSS[Z]");
  const formattedEndDate = endDate.format("YYYY-MM-DD HH:mm:ss.SSSSSS[Z]");

  return useQuery({
    queryKey: ["requests", "date", startDate, endDate],
    queryFn: async () => {
      const response = await axios.get("/api/request", {
        params: {
          approved: "True",
          start_date: formattedStartDate,
          end_date: formattedEndDate,
        },
      });
      return response;
    },
  });
}

export function getWarehouseInfo() {
  return useQuery({
    queryKey: ["warehouse"],
    queryFn: async () => {
      const response = await axios.get("/api/warehouse");
      return response;
    },
  });
}

export function getUserData() {
  return useQuery({
    queryKey: ["user"],
    queryFn: async () => {
      const response = await axios.get("/api/user");
      return response;
    },
  });
}

export function submitUserData(username, password, queryClient) {
  return useMutation({
    mutationFn: async () => {
      const user = {
        username: username,
        password: password,
      };

      const response = await axios.post("/token/", user, {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      });
      console.log(response.data.access);
      if (!response.data.access) {
        throw new Error("Network response was not ok");
      }

      queryClient.setDefaultOptions({
        headers: {
          Authorization: `Bearer ${response.data.access}`,
        },
      });

      return response.data;
    },
  });
}
