The returned object exposes the following properties.

`Succeeded`
:   A `boolean` property that indicates whether or not the authentication attempt was successful.
`Principal`
:   If the authentication succeeds, this property contains the @System.Security.Claims.ClaimsPrincipal (a collection of statements about the authenticated user) returned by the Security System.
`Error`
:   If the authentication fails, this property contains the resulting @System.Exception.  