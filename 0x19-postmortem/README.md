## SUMMARY
During the last server downtimw whic occured at around 1000 hrs 03.05.2021, and lasted until about 1200hrs same day.
The ecommerce application on thger server went down and users experienced either unresponsive site or server error issue.
This issue mainly 90% of users visiting the site from around 1000hrs GMT+1.
The cause of this downtime was due to unprecedented traffic at our black friday event.

## TIMELINE
Issue was detected at around 1010hrs GMT+1 after datadog sent a monitor alert. Upon getting the excessive requests, we took down the server to enable us profer 
fast and immediate solutions. We escalated to the devops team and finance after which we got funding to quickly obtain cloud servers to scale up for the mean time
while setting up a load balancer to distribute traffic.

## ROOT CAUSE
RCA showed that lack of a second server to handle excess traffic was the cause of the downtime.
Issue was fixed by obtaing funds to set up a cloud server instantly and using a load balancer to route traffic appropriately.

## CORRECTIVE ACTION
Moving forward, we need to get two servers and set up a proper load balanced system as data shows that we shoul expect more
traffic in the coming days snce our product is getting popular. Also, we need to set up hourly monitors on a large screen such that every one has access to what is 
happening reraltime.
