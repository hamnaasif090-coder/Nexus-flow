**Project Alpha Deployment Process**

**Prerequisites:**
- Familiarity with Linux operating system and SSH
- Basic knowledge of Node.js, Nginx, and JavaScript programming
- A Slack account (or equivalent communication platform)

**Step 1: Prepare Server for Deployment**

1. **Run the Build Script**: Run `npm run build` to generate the deployment files.
2. **Check Server Status**: Verify that the server is not busy by checking the disk usage with `df -h`. If the disk is full, plan to clean up logs and restart services.

**Step 2: Perform Security Scan**

1. **Run npm Audit**: Run `npm audit` to perform a security scan on the deployment.
2. **Stop Deployment if Audit Fails**: Stop any ongoing deployments if the audit results in errors.

**Step 3: Notify Slack Channel**

1. **Notify Slack before Final Push**: Send notifications to the #deploy-alerts Slack channel before finalizing the deployment.

**Server Setup Commands**

1. **Initialize Nginx Service**: `sudo systemctl init nginx` (to ensure services start automatically)
2. **Restart Nginx Service**: `sudo systemctl restart nginx`

**Troubleshooting Tips**

* If you encounter issues during deployment, review logs to identify potential problems.
* Regularly clean up server disk logs and consider using a tool like rsync to automate cleanup.

**Conclusion**
The Project Alpha Deployment Process aims to streamline the deployment process by standardizing tasks and ensuring compliance with security best practices. By following this SOP, individuals can perform deployments efficiently and effectively without relying on individual expertise.