---
uid: DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.ProviderUserKey
name: ProviderUserKey
type: Property
summary: Returns a user's ID according to the current provider.
syntax:
  content: string ProviderUserKey { get; }
  parameters: []
  return:
    type: System.String
    description: The user name.
seealso: []
---
For Windows Active Directory or Google, the `ProviderUserKey` property value is a Windows user name or a Google account ID, respectively. This value is unique for a specific provider, but different providers can have matching keys.

The @DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.LoginProviderName and `ProviderUserKey` form a unique combination. The `ProviderUserKey` is not necessarily unique among all providers but is always unique for a specific provider.

To support this unique combination, XAF does the following:
* Applies the `Indexed` attribute in XPO-based applications.
* Specifies that `ISecurityUserLoginInfo.LoginProviderName` and `ISecurityUserLoginInfo.ProviderUserKey` pairs should be unique in any override of the `MySolutionDbContext.OnModelCreating` method:

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Security;
    // ... 
    public class MySolutionDbContext : DbContext {
        //...
        public DbSet<ApplicationUser> Users { get; set; }
        public DbSet<ApplicationUserLoginInfo> UserLoginInfos { get; set; }
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            base.OnModelCreating(modelBuilder);
            modelBuilder.Entity<ApplicationUserLoginInfo>(b => {
                b.HasIndex(nameof(ISecurityUserLoginInfo.LoginProviderName), 
                    nameof(ISecurityUserLoginInfo.ProviderUserKey)).IsUnique();
            });
        }
    }
    ```
    ***
