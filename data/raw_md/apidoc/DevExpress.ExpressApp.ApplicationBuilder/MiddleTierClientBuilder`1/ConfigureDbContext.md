---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.ConfigureDbContext(System.Action{Microsoft.EntityFrameworkCore.DbContextOptionsBuilder{`0}})
name: ConfigureDbContext(Action<DbContextOptionsBuilder<TDbContext>>)
type: Method
summary: Configures `DbContext` options for the Middle Tier client.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> ConfigureDbContext(Action<DbContextOptionsBuilder<TDbContext>> configure)
  parameters:
  - id: configure
    type: System.Action{Microsoft.EntityFrameworkCore.DbContextOptionsBuilder{{TDbContext}}}
    description: A delegate thar configures @Microsoft.EntityFrameworkCore.DbContextOptions.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder{{TDbContext}}
    description: The builder that allows you to further configure the Middle Tier client.
seealso:
- linkId: "404389"
- linkId: "404398"
---
