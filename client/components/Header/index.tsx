import React from 'react';
import { makeStyles, AppBar, Toolbar, Container } from '@material-ui/core';

import { Logo } from './Logo';
import { Favorites } from './Favorites';

const useStyles = makeStyles((theme) => ({
  appBar: {
    background: theme.palette.common.white,
    boxShadow: 'none',
  },
  container: {
    padding: 0,
  },
  toolbar: {
    display: 'flex',
    minHeight: '74px',
    [theme.breakpoints.down('sm')]: {
      paddingLeft: 0,
    },
  },
  logo: {
    flex: 1,
  },
}));

export const Header: React.FC = () => {
  const s = useStyles();

  return (
    <AppBar className={s.appBar} position="fixed">
      <Container className={s.container}>
        <Toolbar className={s.toolbar}>
          <Logo className={s.logo} />
          <Favorites />
        </Toolbar>
      </Container>
    </AppBar>
  );
};
