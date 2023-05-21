import React, { useState } from 'react'
import { Coffee } from 'react-feather'
import Button from '../shared/Button'
import Modal from '../shared/Modal'
import CoffeeMachineGif from '../../media/coffee-machine-lineal.gif'

const CoffeeIcon = () => {
  const [show, setShow] = useState(false)
  const onClick = () => {
    setShow(true)
  }

  return (
    <div>
      <Button
        onClick={onClick}
        toolTip="Buy me a coffee"
        style={{ border: 0 }}
        icon={<Coffee />}
      />
      <Modal
        onClose={() => setShow(false)}
        title="Team Netsurfers"
        className="modal-setting"
        show={show}
        showCloseIcon={false}
      >
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          I hope you all enjoy using the project. 
          <img
            src={CoffeeMachineGif}
            alt="coffee machine"
            style={{
              height: 150,
              objectFit: 'contain',
            }}
          />
        </div>

        <div
          style={{
            display: 'flex',
            width: '100%',
            justifyContent: 'flex-end',
            alignItems: 'center',
            gap: '12px',
          }}
        >
          <Button onClick={() => setShow(false)}>Cancel</Button>
          <a
            href=""
            target="_blank"
            rel="noreferrer"
          >
            <Button border onClick={() => setShow(false)}>
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'center',
                  alignItems: 'center',
                  gap: '8px',
                }}
              >
                More Info
              </div>
            </Button>
          </a>
        </div>
      </Modal>
    </div>
  )
}

export default CoffeeIcon
