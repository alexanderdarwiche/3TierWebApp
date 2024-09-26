# Dockerfile for frontend (React)
FROM node:16

# Set working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the app code
COPY . .

# Build the React app
RUN npm run build

# Use a simple web server to serve the built app
RUN npm install -g serve
CMD ["serve", "-s", "build"]

# Expose port 3000
EXPOSE 3000
