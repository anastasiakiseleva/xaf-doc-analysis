---
uid: DevExpress.ExpressApp.ApplicationBuilder.IMiddleTierClient`1
name: IMiddleTierClient<TDbContext>
type: Interface
summary: Declares the API for a Middle Tier client.
syntax:
  content: 'public interface IMiddleTierClient<TDbContext> : IDisposable where TDbContext : DbContext'
  typeParameters:
  - id: TDbContext
    description: The type of `DbContext`.
seealso:
- linkId: DevExpress.ExpressApp.ApplicationBuilder.IMiddleTierClient`1._members
  altText: IMiddleTierClient<TDbContext> Members
- linkId: "404389"
- linkId: "404398"
---
To create a Middle Tier client, configure its settings with the @DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1 and call the @DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.Build method. Once created, the client is immutable.

```csharp
// Configures client `DbContext` type, server, and authentication settings
var builder = new MiddleTierClientBuilder<MainDemoDbContext>()
    .UseServer("http://localhost:5000/")
    .UsePasswordAuthentication("user", "password");

// Creates a Middle Tier client instance
IMiddleTierClient<MainDemoDbContext> client = builder.Build();

// Creates DbContext and operates data
using(var ctx = client.CreateDbContext()) {
    var data = ctx.Users.ToList();
    // ...
}

// Disposes the client
// Note that it is necessary to manually dispose the client when its instance is no longer needed
client.Dispose();
```

[`MiddleTierClientBuilder`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1
[`UseServer`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseServer(System.String)
[`Build`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.Build
[`UsePasswordAuthentication`]: xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UsePasswordAuthentication*
[`CreateDbContext`]: xref:DevExpress.ExpressApp.ApplicationBuilder.IMiddleTierClient`1.CreateDbContext