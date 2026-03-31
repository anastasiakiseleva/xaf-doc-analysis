---
uid: "404401"
seealso:
- linkId: "119064"
title: 'Configure Authentication in an Application With EF Core Middle Tier Security'
---

# Configure Authentication in an Application With EF Core Middle Tier Security

## Configure Authentication on the Server Side

Authentication in the EF Core Middle Tier Security server is implemented similarly to that of the [Backend Web API Service](xref:403394). The Middle Tier Security supports the same authentication methods and uses the same configuration options. For more information on how to configure authentication on the server side, refer to the following article: [Authenticate Web API](xref:403413).

## Configure Authentication in the Client WinForms Application

The XAF Solution Wizard can generate code for the following authentication methods:

- Standard authentication (login/password authentication based on JWT)
- Windows authentication

In an existing WinForms application, you can enable these authentication methods as follows.

### Standard authentication

Edit the client WinForms application's `Startup.cs` file to configure the security system as shown below.

# [C#](#tab/tabid-csharp)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory { 
    public static WinApplication BuildApplication(string connectionString) { 
        var builder = WinApplication.CreateBuilder(); 
        // ... 
        builder.Security 
            .UseMiddleTierMode(options => { 
                options.BaseAddress = new Uri(...); 
                options.Events.OnHttpClientCreated = client => client.DefaultRequestHeaders.Add("Accept", "application/json"); 
                options.Events.OnCustomAuthenticate = (sender, security, args) => { 
                    args.Handled = true; 
                    HttpResponseMessage msg = args.HttpClient.PostAsJsonAsync("api/Authentication/Authenticate", (AuthenticationStandardLogonParameters)args.LogonParameters).GetAwaiter().GetResult(); 
                    string token = (string)msg.Content.ReadFromJsonAsync(typeof(string)).GetAwaiter().GetResult(); 
                    if(msg.StatusCode == HttpStatusCode.Unauthorized) { 
                        throw new UserFriendlyException(token); 
                    } 
                    msg.EnsureSuccessStatusCode(); 
                    args.HttpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("bearer", token); 
                }; 
            }) 
            .UsePasswordAuthentication(); 
        // ... 
     } 
} 
```
***

In the above code sample, the `api/Authentication/Authenticate` URL is the path to the authentication endpoint. See the following article for more information: [Configure the JWT Authentication for the Web API](xref:403504#step-4-add-a-jwt-authentication-service).

### Windows authentication

Edit the client WinForms application's `Startup.cs` file to configure the security system as shown below.

# [C#](#tab/tabid-csharp)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory { 
    public static WinApplication BuildApplication(string connectionString) { 
        var builder = WinApplication.CreateBuilder(); 
        // ... 
        builder.Security 
            .UseMiddleTierMode(options => { 
                options.BaseAddress = new Uri(...); 
            }) 
            .UseWindowsAuthentication(); 
        // ... 
     } 
} 
```
***

## Access Token Lifetime

The XAF Middle Tier server application uses JWT authentication. Each access token has a limited lifetime; after this period, the server marks it as invalid. For security, the server does not issue long-lived access tokens. Instead, it refreshes tokens when needed.

## Use Custom Authentication Methods

If you need to implement a custom authentication method in your application, follow the general steps below:

1. Configure the Middle Tier Security project to use the required authentication method.

2. Implement a corresponding endpoint on the Middle Tier Security server side.

3. On the WinForms client application side, all the necessary settings are made at the stage when the HTTP client is configured. To do this, handle the following events available through the `ApplicationBuilder` extension methods:

- [MiddleTierSecurityEvents.OnCustomCreateHttpClient](xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents.OnCustomCreateHttpClient)

- [MiddleTierSecurityEvents.OnHttpClientCreated](xref:DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents.OnHttpClientCreated)

All interactions between the client application and the Middle Tier Security server are done through the HTTP/HTTPS protocol with an HTTP client. You can configure the HTTP client's settings (timeouts, base URL and so on) in handlers for the events described above.

## Grant Anonymous Access to Types

The Middle Tier Security can be configured to allow a client to read business objects of the specified types without authentication/authorization. In such instances, all read operations are performed regardless of the Security System's restrictions.

To allow anonymous read operations on business objects of the specified types, add the following code to the `Startup.ConfigureServices` method call in the Middle Tier Security project's `Startup.cs` file.

# [C#](#tab/tabid-csharp)

```csharp
public class Startup { 
    public void ConfigureServices(IServiceCollection services) { 
        //...
        services.AddXafMiddleTier(Configuration, builder => {
            //...
            builder.Security
                .UseIntegratedMode(options => {
                    //...
                    options.Events.OnSecurityStrategyCreated = securityStrategy => {
                        ((SecurityStrategy)securityStrategy).AnonymousAllowedTypes.Add(typeof(ObjectType));
                    };
                })
                .AddPasswordAuthentication(options => options.IsSupportChangePassword = true);
            //...
        });
    }
} 
```
***

## Implement Additional Functionality

Similar to the [Backend Web API Service](xref:403394), the Middle Tier Service allows you to implement custom API endpoints that you can use to add functionality to the service. Refer to the following article for more information on how to do this: [Create Custom Endpoints](xref:403858).