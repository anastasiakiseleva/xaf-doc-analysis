**File:** _MySolution.Blazor\API\Security\AuthenticationController.cs_

# [C#](#tab/tabid-csharp)

```csharp{17,27,29,34}
using DevExpress.ExpressApp.Security;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using Swashbuckle.AspNetCore.Annotations;
using System.IdentityModel.Tokens.Jwt;
using System.Text;

namespace MySolution.WebApi.Jwt;

[ApiController]
[Route("api/[controller]")]
public class AuthenticationController : ControllerBase {
    readonly SignInManager signInManager;
    readonly IConfiguration configuration;

    public AuthenticationController(SignInManager signInManager, IConfiguration configuration) {
        this.signInManager = signInManager;
        this.configuration = configuration;
    }

    [HttpPost("Authenticate")]
    public IActionResult Authenticate(
        [FromBody]
            [SwaggerRequestBody(@"For example: <br /> { ""userName"": ""Sam"", ""password"": """" }")]
            AuthenticationStandardLogonParameters logonParameters
    ) {
        var authenticationResult = signInManager.AuthenticateByLogonParameters(logonParameters);

        if(authenticationResult.Succeeded) {
            var issuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(configuration["Authentication:Jwt:IssuerSigningKey"]!));
            var token = new JwtSecurityToken(
                issuer: configuration["Authentication:Jwt:ValidIssuer"],
                audience: configuration["Authentication:Jwt:ValidAudience"],
                claims: authenticationResult.Principal.Claims,
                expires: DateTime.Now.AddHours(2),
                signingCredentials: new SigningCredentials(issuerSigningKey, SecurityAlgorithms.HmacSha256)
                );
            return Ok(new JwtSecurityTokenHandler().WriteToken(token));
        }
        return Unauthorized("User name or password is incorrect.");
    }
}
```
***