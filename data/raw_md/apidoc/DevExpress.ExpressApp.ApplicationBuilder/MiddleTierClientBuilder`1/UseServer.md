---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseServer(System.String)
name: UseServer(String)
type: Method
summary: Specifies the base Middle Tier server address.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> UseServer(string baseAddress)
  parameters:
  - id: baseAddress
    type: System.String
    description: The server web address (URL).
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