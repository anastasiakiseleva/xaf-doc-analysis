---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UsePasswordAuthentication(System.String,System.String)
name: UsePasswordAuthentication(String, String)
type: Method
summary: Configures the client to use authentication with the specified login and password.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> UsePasswordAuthentication(string userName, string password)
  parameters:
  - id: userName
    type: System.String
    description: The client user name (login).
  - id: password
    type: System.String
    description: The client password.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder{{TDbContext}}
    description: The builder that allows you to further configure the Middle Tier client.
seealso:
- linkId: "404389"
- linkId: "404398"
---
The following code sample creates a new client, connects it to the remote Middle Tier server at http://localhost:5000/, and uses authentication with the specified login and password.

```csharp
var builder = new MiddleTierClientBuilder<MainDemoDbContext>()
    .UseServer("http://localhost:5000/")
    .UsePasswordAuthentication("user", "password");

IMiddleTierClient<MainDemoDbContext> client = builder.Build();
```