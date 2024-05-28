# Use an official .NET Core runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base

# Install Apache
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

# Enable required Apache modules
RUN a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests

# Set the working directory
WORKDIR /NetAppDocker

# Copy the .NET application
COPY NetAppFiles /NetAppDocker

# Copy the Apache configuration file
COPY default.conf /etc/apache2/sites-available/000-default.conf

# Ensure the ASP.NET Core app uses Kestrel on port 5000
ENV ASPNETCORE_URLS=http://+:5000

# Expose port 80 for Apache and port 5000 for the .NET application
EXPOSE 80 5000

# Start the .NET application and Apache server
# !! Already in the NetAppDocker
CMD ["sh", "-c", "dotnet bin/Debug/net8.0/NetAppFiles.dll & apachectl -D FOREGROUND"]
