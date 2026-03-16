---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1
name: MiddleTierClientBuilder<TDbContext>
type: Class
summary: Configures a client for a Middle Tier server with a specified `DbContext` type.
syntax:
  content: |-
    public class MiddleTierClientBuilder<TDbContext>
        where TDbContext : DbContext
  typeParameters:
  - id: TDbContext
    description: The type of a `DbContext` object.
seealso:
- linkId: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1._members
  altText: MiddleTierClientBuilder<TDbContext> Members
- linkId: "404389"
- linkId: "404398"
---
Use `MiddleTierClientBuilder` to configure and create an immutable client for a Middle Tier server. Ensure all configurations are set before creation. Once created, the client cannot be modified.

* Call the @DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseServer(System.String) method to specify the base Middle Tier server address. 
* Call one of the following methods to configure the client authentication method:
    * @DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UsePasswordAuthentication*
    * @DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseTokenAuthentication*
    * @DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseWindowsAuthentication

  Note that one Middle Tier client can only use one authentication method. To support multiple methods, use different `MiddleTierClientBuilder` objects to create separate clients for each authentication method.

The following code sample creates a new client connected to the remote Middle Tier server at http://localhost:5000/ and specifies authentication login and password.

```csharp
var builder = new MiddleTierClientBuilder<MainDemoDbContext>()
    .UseServer("http://localhost:5000/")
    .UsePasswordAuthentication("user", "password");

IMiddleTierClient<MainDemoDbContext> client = builder.Build();
```
