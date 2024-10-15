def myvars(G):
    jupyterlab_vars = ('In', 'Out', 'quit', 'exit', 'open', 'get_ipython')
    vs = {k: v for k, v in G.items()
          if k == '_' or not k.startswith('_') and k not in jupyterlab_vars
          }
    display(vs)