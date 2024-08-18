
# Postmortem Report: Apache Server 500 Internal Server Error Outage



## Issue Summary
`Duration`: August 17, 2024, 14:00 - August 17, 2024, 16:30 UTC

`Impact`: The Apache web server was returning a 500 Internal Server Error for the company's main website. This outage affected 100% of users trying to access the website during the downtime, resulting in complete unavailability of the service.

`Root Cause`: The server was unable to find necessary .php files due to incorrect file extensions (.phpp instead of .php) in the WordPress configuration file.

# Timeline
- 14:00 UTC: Issue detected; users reported an error when accessing the website.

- 14:05 UTC: Monitoring systems alerted the team to a high number of 500 errors.

- 14:10 UTC: An engineer started investigating the Apache error logs and traced file access issues.

- 14:20 UTC: strace was used to monitor system calls and revealed the server was looking for files with a .phpp extension.

- 14:40 UTC: The root cause was identified as a misconfiguration in the wp-settings.php file, which had incorrect file extensions.

- 14:50 UTC: An initial fix was applied manually using sed to replace .phpp with .php in the wp-settings.php file.

- 15:00 UTC: The fix was verified, and the website was accessible again.

- 15:30 UTC: Incident was fully resolved and monitoring confirmed normal operation.

- 16:00 UTC: Post-incident review and documentation of the fix.
## Root Cause and Resolution

`Root Cause`: The Apache server was configured to reference .phpp files instead of .php due to an error in the WordPress configuration file (wp-settings.php). This mismatch caused Apache to fail when trying to include or access these files, leading to 500 Internal Server Errors.

`Resolution`: The issue was resolved by updating the wp-settings.php file to use the correct .php file extension. The fix was applied manually with a sed command and then automated using a Puppet manifest to prevent recurrence.

## Corrective and Preventative Measures
- Improvements:

    - Implement automated configuration validation checks for file extensions in critical configuration files.
    - Enhance error handling and logging to capture such configuration errors early in the development or staging environments.

- Tasks:

    - Patch Configuration: Update the Puppet manifest to ensure that incorrect file extensions are corrected automatically.
    - Add Monitoring: Implement monitoring for file existence and correctness in the web application directory.
    - Review Deployment Processes: Conduct a review of deployment scripts and processes to ensure that file names and extensions are validated before going live.
    - Enhance Logging: Improve logging to include detailed error messages for configuration 
