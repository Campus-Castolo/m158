# Project Planning

## Forming a team
| Team Name       | Member 1       | Member 2              |
|-----------------|----------------|-----------------------|
| LazyFirefox9882 | Rayan Lee Bopp | Florian Merlin Fröbel |

## Project planning

### 1. Preliminary Assessment:
Before migrating any service it is important to do a preliminary assessment of the existing service.

For example this can be achieved by identifying what needs to be migrated (Data, Plugins, Themes, etc.)

Now to find out what Data needs to be transfered. For this one could make a SQL dump file from the existing Wordpress database and just insert it into the new one.

As for the Plugins it is important to know what Plugins the site currently uses, this can be checked by doing the following:

    Step 1: Log in with your credentials.
    Step 2: Go to “System Definition”.
    Step 3: Click on “Plugins”.
    Step 4: Check the names and descriptions.
    Step 5: Use search, if needed.

### 2. Set Clear Objectives:
Setting a clear objective in any situation is a must, especially when you are planning a website migraiton from host to another host.

However defining goals requires a deep understand of the overlaying subject. In this instance it is advised to have a basic understanding of how a migration is executed and how a wordpress site operates.

Below are the basic necessary steps to complete a migration of a wordpress website with the end goal of **migrating the wordpress website from the former host to the new host, including the database and all the plugins itself.** In our case this would be worded like the following: ***"We want to migrate the wordpress website from the former host onto the proxomox enviornment with the old dataset and plugins"***

1. Content Preservation 
2. Functionality Maintenance
3. SEO Preservation
4. Data Integrity and Security
5. Documentation and Backup

These are 5 common practices when migrating a wordpress website according to guides and other specialists.

- Outline any additional features or improvements desired.

Additionally one could look into known voulnerabilites in plugins and swap them out for similar ones. This would the main point of concern in point 4 `4. Data Integrity and Security.`

### 3. Choose a New Hosting Provider:
For this step it is crucial to weigh each aspects against eachother. For example if you want to migrate the wordpress website onto the cloud it is important to compare the two or even three different cloud providers with eachother however, this would be done by making a table a comparing functionality based on categories. This would look something akin to this:

| **Feature**          | **AWS**                            | **Azure**                                  | **Alibaba Cloud**                         |
|----------------------|------------------------------------|--------------------------------------------|-------------------------------------------|
| **Cloud Services**   | Widest range of services           | Comprehensive services portfolio           | Growing portfolio of services             |
| **Global Reach**     | Extensive global presence          | Global data center footprint               | Rapidly expanding globally                |
| **Market Share**     | Largest market share               | Second-largest market share                | Growing presence globally                 |
| **Compute Services** | EC2, Lambda, ECS, EKS              | Virtual Machines, App Service              | ECS, Elastic Compute Service              |
| **Storage Services** | S3, EBS, Glacier                   | Blob Storage, Disk Storage                 | Object Storage, OSS                       |
| **Pricing Model**    | Pay-as-you-go, usage-based pricing | Similar to AWS, usage-based                | Competitive pricing models                |
| **Networking**       | VPC, Direct Connect, Route 53      | Virtual Network, ExpressRoute              | Virtual Private Cloud, VPC                |
| **Database**         | RDS, DynamoDB, Aurora              | SQL Database, Cosmos DB                    | ApsaraDB, PolarDB                         |
| **AI/ML Services**   | SageMaker, Rekognition, Polly      | Azure Machine Learning, Cognitive Services | Machine Learning Platform, MaxCompute, AI |
| **IoT**              | AWS IoT Core, Greengrass           | Azure IoT Hub, IoT Edge                    | IoT Platform                              |

However this isn't important to us, since we were generously provided a proxomox enviornment on which we can host our client and server.
Our server is a Ubuntu server and our client is a Windows 10 client. 

### 5. Migration Process:
- Document step-by-step procedures for migrating the database, themes, plugins, and media files.
- Address potential issues and create contingency plans.
- Make a graphic to represent the migration progress (rough)

### 6. Theme and Plugin Compatibility:
- Check and update themes and plugins for compatibility with the new WordPress version.

### 7. SEO Considerations:
- Redirect old URLs to new ones to maintain SEO.
- Update sitemaps and inform search engines of the migration.

### 8. Communication Plan:
- Inform stakeholders, including users, about the migration plan.
- Provide detailed instructions for any necessary actions on their part.
- What happens if any unforseen actions occur (make graphic for this highlighting the rough communication)

### 9. Post-Migration Monitoring:
- Have a general plan for monitoring but refine it based on post-migration feedback and observations.

---

# Navigation

[Back to Main](../README.md)

[To Wiki](https://github.com/Campus-Castolo/m158/wiki/)
