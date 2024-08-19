
![Untitled](https://github.com/user-attachments/assets/f104ea34-e9b2-4e7f-83d8-63d18d5e7a3b)


# Our journey from chaos to clarity.



## Issue Summary📝
`Duration`: August 17, 2024, 14:00 - August 17, 2024, 16:30 UTC

`Impact`: Our website turned into a digital ghost town👻, with users greeted by the dreaded 500 Internal Server Error. Every visitor was met with an empty, error-riddled page. This outage left 100% of our users unable to access the site. Not fun!

`Root Cause`: 🔎🫚The server was unable to find necessary .php files due to incorrect file extensions (.phpp instead of .php) in the WordPress configuration file.

# Timeline⏱️
- 14:00 UTC: Panic Mode Activated. Users started reporting that our website was down. “Why does it always happen on weekends?” was the collective sigh from the team.

- 14:05 UTC: Monitoring alerts flashed bright red. It was not a drill.

- 14:10 UTC: Our tech wizard 👩‍💻 dove into the Apache error logs. “I see dead files,” he declared.
- 14:20 UTC: `strace` was summoned. Like a digital detective, it traced the system calls and revealed our server’s tragic flaw: it was looking for .phpp files instead of .php.

- 14:40 UTC: The root cause was uncovered – a configuration snafu in the `wp-settings.php `file. It had been calling for .phpp files. A case of mistaken identity, but not a pretty one.

- 14:50 UTC: The fix was applied manually using sed. The website was back in action. Cue the celebratory confetti!

- 15:00 UTC: Normal service resumed. Users could now visit the site without encountering the infamous 500 error.

- 15:30 UTC: The team wrapped up the incident with high fives and a fresh round of coffee.

- 16:00 UTC: The post-incident review went live, including this snazzy postmortem.
## Root Cause and Resolution🔬

`Root Cause`: Our WordPress configuration file (wp-settings.php) had a simple but fatal typo: .phpp instead of .php. The server was looking for files that didn’t exist, leading to those dreaded 500 errors. It's like expecting a pizza delivery and getting an empty box.

`Resolution`: We corrected the typo with a sed command and made sure it wouldn’t happen again by automating the fix with Puppet. The server now knows the difference between .php and .phpp.

## Corrective✅ and Preventative ✋Measures
- Improvements:

    - Implement automated checks to catch such typos before they cause chaos. Let’s avoid more pizza box situations.
    - Enhance logging and error messages to quickly spot configuration blunders in staging.

- Tasks:

    - Patch Configuration: Update the Puppet manifest to ensure that incorrect file extensions are corrected automatically.
    - Add Monitoring: Implement monitoring for file existence and correctness in the web application directory.
    - Review Deployment Processes: Conduct a review of deployment scripts and processes to ensure that file names and extensions are validated before going live.
    - Enhance Logging: Improve logging to include detailed error messages for configuration 


