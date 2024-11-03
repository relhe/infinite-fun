# Use an official Node.js image as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose port 3000 and start the application
EXPOSE 3000
CMD ["npm", "run", "dev"]
