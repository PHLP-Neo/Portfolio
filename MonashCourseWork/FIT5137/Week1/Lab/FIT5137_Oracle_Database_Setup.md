# FIT5137 Advanced Database Technology

## Oracle Database Setup for Weeks 1–7

### Monash Oracle Service Access

For this unit, Oracle Database will be used during **Weeks 1–7**. Choose one of the following database management tools:

- **DBeaver** — recommended because it will continue to be used for the spatial database section in Weeks 8–12.
- **Visual Studio Code with the Oracle SQL Developer extension** — the same software used in FIT9132, FIT2094, or FIT3171.

From **Weeks 8–12**, the unit will transition to a spatial database using **PostgreSQL** (also known as Postgres), a free and open-source relational database management system that emphasises extensibility and SQL compliance.

All spatial database exercises and demonstrations will use DBeaver because Visual Studio Code has limited spatial-data visualisation capabilities.

> **Important:** A Monash VPN connection is required when connecting to the Oracle database during Weeks 1–7.

---

## DBeaver

### Running DBeaver for the First Time

1. Download the DBeaver Community Edition from:
   <https://dbeaver.io/download/>
2. Extract the downloaded archive or install the application.
3. Run `dbeaver`.
4. If DBeaver asks whether you want to create a sample database, select **No**.
5. DBeaver is now ready to use.

### Connecting DBeaver to the Oracle Server

1. Click **New Database Connection** in the upper-left corner.

   > Your version of DBeaver may look different from the version shown in the original setup guide.

2. Select **Oracle** from the available database options.
3. Enter the following connection parameters:

| Setting | Value |
|---|---|
| Host | `fit-oracle-pt01.mpc.monash.edu` |
| Database / Service Name | `FIT5137.fit-oracle-pt01.mpc.monash.edu` |
| Port | `1521` |
| Username | `S` followed by your student ID |
| Initial password | `student` |

4. Click **Test Connection**.
5. A successful test should confirm that DBeaver has connected to the Oracle server.
6. If the connection test produces another response, ask your lab demonstrator.
7. Click **Finish** to save the connection configuration.
8. Change the default password after making the first connection.

> **Lab computers:** Connection configurations are not stored permanently, so these steps must be repeated when using a lab computer.

### Creating a New SQL Workspace

1. Open the **SQL** toolbar.
2. Select **New SQL Script**.

---

## Visual Studio Code

The installation process is the same as in FIT2094, FIT3171, and FIT9132, so it is not repeated in the original setup guide.

Use the following Oracle connection details:

| Setting | Value |
|---|---|
| Connection name | `FIT5137` |
| Hostname | `fit-oracle-pt01.mpc.monash.edu` |
| Port | `1521` |
| Connection type | `Service Name` |
| Service name | `FIT5137.fit-oracle-pt01.mpc.monash.edu` |
| Username | `S` followed by your student ID |
| Initial password | `student` |

Change the default password after making the first connection.
